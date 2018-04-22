$(function(){
	$('#btnSignUp').click(function(){

		$.ajax({
			url: '/post',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
})
