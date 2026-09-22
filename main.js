(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nav=document.querySelector('.nav'), burger=document.querySelector('.burger'), links=document.querySelector('.nav-links');

  // menu mobilne
  if(burger){
    burger.addEventListener('click', function(){
      var open=links.classList.toggle('open'); burger.classList.toggle('x', open);
      burger.setAttribute('aria-expanded', open); document.body.style.overflow=open?'hidden':'';
    });
    links.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){
      links.classList.remove('open'); burger.classList.remove('x'); document.body.style.overflow='';
    });});
  }

  // nagłówek hero: słowo po słowie z rozmycia
  document.querySelectorAll('[data-split]').forEach(function(el){
    var i=0;
    (function walk(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(n){
        if(n.nodeType===3){
          var frag=document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function(part){
            if(!part) return;
            if(/^\s+$/.test(part)){ frag.appendChild(document.createTextNode(' ')); return; }
            var w=document.createElement('span'); w.className='w'; w.style.setProperty('--i', i++); w.textContent=part; frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if(n.nodeType===1 && n.tagName!=='BR'){ walk(n); }
      });
    })(el);
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ el.classList.add('in'); }); });
  });

  // liczniki
  function count(el){
    var end=+el.dataset.count, t0=null;
    if(reduce){ el.textContent=end; return; }
    function tick(t){ if(!t0) t0=t; var p=Math.min((t-t0)/1600,1); el.textContent=Math.round(end*(1-Math.pow(1-p,3))); if(p<1) requestAnimationFrame(tick); }
    requestAnimationFrame(tick);
  }

  // wejścia przy przewijaniu
  var targets=document.querySelectorAll('.rv,.stag');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){
      if(!e.isIntersecting) return;
      e.target.classList.add('in');
      e.target.querySelectorAll('[data-count]').forEach(count);
      io.unobserve(e.target);
    });},{threshold:.15, rootMargin:'0px 0px -60px 0px'});
    targets.forEach(function(el){ io.observe(el); });
  } else { targets.forEach(function(el){ el.classList.add('in'); }); }

  // proces: aktywny krok = ten na środku ekranu, zdjęcie się podmienia
  var steps=document.querySelectorAll('.step'), media=document.querySelector('.proc-media');
  var layers=media?media.querySelectorAll('.pm'):[], counter=media?media.querySelector('.proc-count span'):null, active=-1;
  function setStep(i){
    if(i===active) return; active=i;
    steps.forEach(function(s,k){ s.classList.toggle('on', k===i); });
    layers.forEach(function(l,k){ l.classList.toggle('on', k===i); });
    if(counter) counter.textContent='0'+(i+1);
    if(media) media.classList.toggle('ai-on', i===2);
  }

  // karty case: przyklejają się i lekko maleją, gdy najeżdża następna
  var cards=document.querySelectorAll('.stack .case');
  cards.forEach(function(c,i){ c.style.setProperty('--i', i); });

  var hero=document.querySelector('.hero-bg'), heroH=hero?hero.parentNode.offsetHeight:0, ticking=false;
  function frame(){
    ticking=false;
    var y=window.scrollY, vh=window.innerHeight, desk=window.innerWidth>1000;
    if(nav) nav.classList.toggle('scrolled', y>60);
    if(reduce) return;
    if(hero && y<heroH+200) hero.style.transform='translate3d(0,'+(y*0.45).toFixed(1)+'px,0)';
    if(steps.length && desk){
      var mid=vh*0.5, best=0, bd=1e9;
      steps.forEach(function(s,k){ var r=s.getBoundingClientRect(), d=Math.abs(r.top+r.height/2-mid); if(d<bd){bd=d;best=k;} });
      setStep(best);
    }
    if(window.innerWidth>820){
      cards.forEach(function(c,i){
        var next=cards[i+1]; if(!next){ c.style.transform=''; return; }
        var top=c.getBoundingClientRect().top, nt=next.getBoundingClientRect().top;
        var p=Math.min(Math.max(1-(nt-top)/(c.offsetHeight),0),1);
        c.style.transform='scale('+(1-p*0.05).toFixed(4)+')';
        c.style.filter='brightness('+(1-p*0.08).toFixed(3)+')';
      });
    } else { cards.forEach(function(c){ c.style.transform=''; c.style.filter=''; }); }
  }
  function onScroll(){ if(!ticking){ ticking=true; requestAnimationFrame(frame); } }
  window.addEventListener('scroll', onScroll, {passive:true});
  window.addEventListener('resize', function(){ heroH=hero?hero.parentNode.offsetHeight:0; onScroll(); });
  if(steps.length) setStep(0);
  frame();

  // formularz pokazowy
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit', function(ev){ ev.preventDefault(); f.classList.add('sent'); var b=f.querySelector('button'); b.textContent='Wysłano (wersja pokazowa)'; b.disabled=true; });
  });
})();
