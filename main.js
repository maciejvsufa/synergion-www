(function(){
  var nav=document.querySelector('.nav'), burger=document.querySelector('.burger'), links=document.querySelector('.nav-links');
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', window.scrollY>60); }
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  if(burger){
    burger.addEventListener('click', function(){
      var open=links.classList.toggle('open'); burger.classList.toggle('x', open);
      burger.setAttribute('aria-expanded', open); document.body.style.overflow=open?'hidden':'';
    });
    links.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){
      links.classList.remove('open'); burger.classList.remove('x'); document.body.style.overflow='';
    });});
  }

  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function count(el){
    var end=+el.dataset.count, t0=null;
    if(reduce){ el.textContent=end; return; }
    function tick(t){ if(!t0) t0=t; var p=Math.min((t-t0)/1400,1); el.textContent=Math.round(end*(1-Math.pow(1-p,3))); if(p<1) requestAnimationFrame(tick); }
    requestAnimationFrame(tick);
  }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){
      if(!e.isIntersecting) return;
      e.target.classList.add('in');
      e.target.querySelectorAll('[data-count]').forEach(count);
      io.unobserve(e.target);
    });},{threshold:.12, rootMargin:'0px 0px -40px 0px'});
    document.querySelectorAll('.rv').forEach(function(el){ io.observe(el); });

    var steps=document.querySelectorAll('.step');
    var so=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting) e.target.classList.add('on'); });},{rootMargin:'0px 0px -35% 0px'});
    steps.forEach(function(s){ so.observe(s); });
  } else {
    document.querySelectorAll('.rv').forEach(function(el){ el.classList.add('in'); });
  }

  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit', function(ev){ ev.preventDefault(); f.classList.add('sent'); var b=f.querySelector('button'); b.textContent='Wysłano (wersja pokazowa)'; b.disabled=true; });
  });
})();
