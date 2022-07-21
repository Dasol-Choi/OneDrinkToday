function connectEvent (data) {
    const {keyword} = data;
    const url = `/search?keyword=${keyword}`;
    $.ajax({
        url: url,
        type: 'get',
        success: function(response){
            window.location.href=url;
        }
    })
}

function submitEvent (e) {
    e.preventDefault();
    const formEl = $(e.currentTarget);
    const keyword = formEl.find('[name="keyword"]').val();

    const data = {
        keyword
    }

    connectEvent(data);
}

function searchFocus () {
    $('.form-control').on('focusin', function () {
        $('.wrap-search').addClass('is-focus');
    })

    $('.form-control').on('focusout', function () {
        $('.wrap-search').removeClass('is-focus')
    })
}

export function search() {
  const searchFormEl = $('#search_cocktail');

  searchFormEl.on('submit', submitEvent);
  searchFocus();
}