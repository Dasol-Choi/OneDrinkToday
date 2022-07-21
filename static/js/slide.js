import {resizeEvent} from './common.js';

let situationSlide=undefined;
let slideLoad=false;
let activeItem=0;
let slideClick=false;

resizeEvent(()=>{
  if( situationSlide !== undefined) {
    situationSlide.destroy();
    situationSlide = undefined;  
    slideLoad=false;
    lstActive(activeItem);
  } 
  $('.lst-situation .btn').on('click',btnEvent)

}, ()=>{
  situationSlide = new Swiper('.bx-situation', {
    wrapperClass: 'lst-situation',
    slideClass: 'item',
    slidesPerView: 3.8,
    direction: 'horizontal',
    loop:true,
    centeredSlides: true,
    slideToClickedSlide:true,
    draggable:true,
    breakpoints: {
      480: {
        slidesPerView: 4.5,
      },
    },
    on: {
      init : function () {
        slideLoad=true;
        $('.lst-situation .btn').off('click', btnEvent);
      },
      slideChange: function () {
        if(slideLoad) {
          activeItem = this.realIndex;
          // console.log('slideChange',activeItem)
        }
      },
      click:function () {
        slideClick = true;
        // $('.lst-situation .item').removeClass('is-active')
        // $('.lst-situation .item').eq(this.clickedIndex).addClass('is-active');
       
        // console.log(this)
      }
    }
  })
  
  situationSlide.on('click', function () {
    setTimeout(() => {
  
    $('.lst-situation .item').removeClass('is-active');
    $('.lst-situation .item').eq(situationSlide.activeIndex).addClass('is-active');
    }, 100);
  })
  situationSlide.slideToLoop(activeItem);
})

function btnEvent (e) {
  const btnEl = $('.lst-situation .btn');
  btnEl.parent('.item').removeClass('is-active');
  $(e.currentTarget).parent('.item').addClass('is-active'); 
  activeItem=$(e.currentTarget).parent('.item').index();
}

function lstActive (activeItem) {
  const listItemEl = $('.lst-situation .item')
  listItemEl.removeClass('is-active');
  listItemEl.eq(activeItem).addClass('is-active');
}