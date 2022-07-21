let cocktailList=[];

// data 10개씩 자르기    
function listPaging (row) {
    cocktailList=[];
    const rowLeng = Math.floor(row.length / 10);

    for(let i=0;i<=rowLeng;i++) {
        let last = 0;
        
        if( i < 10) {
            last = 10*(i+1);
        } else {
            last = (10*i)+10;
        }
        cocktailList.push( row.slice((10*i), 10*(i+1)) );
    }
}

// 마크업 만들기
function makeHTML(row) {
    let HTML = '';
    for(let i in row) {
        const item = row[i];
        let cardClass = '';

        switch ( item.name ) {
            case  `Pimm's Cup (or Classic Pimm's)`:
            case `Mezcal Margarita`:
                cardClass = 'cover';
                break;
            default:
                break;
        }
        
        HTML += `
        <li class="lst-item">
            <a href="/${ encodeURIComponent(item.name).replace(/'/gi, "%27") }" class="card-cocktail ${cardClass}">
                <div class="bx-thumb">
                    <img src="${ item.img }" alt="${ item.name }">
                </div>
                <div class="bx-cocktail-info">
                    <span class="cocktail-en-name">${ item.name }</span>
                    <strong class="cocktail-name">${ item.name_kor }</strong>
                    <p class="cocktail-ingredients">베이스 : ${ item.base_kor }</p>
                </div>
            </a>
        </li>`;
    }

    return HTML;
}

// 페이징 처리
let paging = 0;
let loading = false;
let appendPos = .95;

//바닥에서 마크업 추가
$(window).on('scroll', function(e) {
    const scrollPos = window.innerHeight + window.scrollY;
    const documentHeight = $('body').height() * appendPos;

    if(scrollPos > documentHeight && !loading) {
        loading = true;
        paging++
        const HTML = makeHTML(cocktailList[paging]);
        $('.lst-cocktail').append(HTML)
            .ready(function () {
                loading = false;
            });
    }
});