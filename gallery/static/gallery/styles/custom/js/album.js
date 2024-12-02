$('.album-container').magnificPopup({
	delegate: 'a', // child items selector, by clicking on it popup will open
	type: 'image',
	mainClass: 'mfp-no-margins mfp-with-zoom',
	gallery: {
		enabled: true,
		navigateByImgClick: true,
		preload: [0, 1],
	},
	image: {
		tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
		titleSrc: function (item) {
			return item.el.attr('title');
		},
		verticalFit: true,
	},
	zoom: {
		enabled: true,
		duration: 300, // don't foget to change the duration also in CSS
		easing: 'ease-in-out',
		opener: function (openerElement) {
			// openerElement is the element on which popup was initialized, in this case its <a> tag
			// you don't need to add "opener" option if this code matches your needs, it's defailt one.
			console.log(openerElement);
			return openerElement.is('img')
				? openerElement
				: openerElement.find('img');
		},
	},
	// other options
});
