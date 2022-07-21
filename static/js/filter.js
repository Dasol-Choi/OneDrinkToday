import {resizeEvent} from './common.js';

const btnFilter = $('[data-role="btn-filter"]');
const btnClose = $('[data-role="btn-close"]');
const categoryEl = $('.bx-category');
const dimmedEl = $('.dimmed');

export function filter() {
  btnFilter.on('click', categoryShow);
  dimmedEl.on('click', categoryHide);
  btnClose.on('click', categoryHide);

  resizeEvent(()=>{
    categoryEl.show();
    dimmedEl.hide();

    $('.btn-category').click(function (e) {
      categoryActive(e.currentTarget);
    })
  },()=>{
    categoryHide();    
    
    $('.btn-category').click(function (e) {
      categoryActive(e.currentTarget);
      categoryHide();
    })
  });
}

function categoryShow () {
  categoryEl.show();
  dimmedEl.show();
}

function categoryHide () {
  categoryEl.hide();
  dimmedEl.hide();
}

function categoryActive (target) {
  $('.btn-category').removeClass('is-active');
  $(target).addClass('is-active');
}