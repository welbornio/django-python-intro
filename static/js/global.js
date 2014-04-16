$(function() {

	if (!$('form#add-review').length) {
		return;
	}

	var changeNumStars = function changeNumStars() {
		var numStars, stars, i, glyphClass;
		numStars = parseInt($('#stars').val());
		stars = $('<p>');

		for (i = 0; i < 5; i++) {
			if (i < numStars) {
				glyphClass = 'glyphicon-star';
			}
			else {
				glyphClass = 'glyphicon-star-empty';
			}

			stars.append($('<span>').addClass('glyphicon ' + glyphClass));
		}
		
		$('#num-stars').html(stars);
	};

	$('#stars').on('change', function() {
		changeNumStars();
	});

	changeNumStars();
});