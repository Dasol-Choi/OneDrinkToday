const screen = {
	mobile: 768,
}

export function resizeEvent (pcFunc, moFunc) {
	var statue = '';
	var winW = 0;
	var winH = 0;

	sizeCheck();
	$(window).resize( sizeCheck );

	function sizeCheck () {
		var winWCheck = $(window).outerWidth();
		var winHCheck = $(window).innerHeight();
		
		if(winW !== winWCheck || winH !== winHCheck){ // 모바일에서 아래로 스크롤 했을때 대응.
			winW = winWCheck;
			winH = winHCheck;
			
			if ( winWCheck <= screen.mobile ) {
				if( statue !== 'mobile' ) {
					statue = 'mobile';
					
					moFunc(statue);
				}
			} 
			else {
				if( statue !== 'pc' ) {
					statue = 'pc';

					pcFunc();
				}
			} 
		}
	}
}