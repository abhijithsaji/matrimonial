/*price range*/

 $('#sl2').slider();

	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};	
		
/*scroll to top*/

$(document).ready(function(){
	$(function () {
		$.scrollUp({
	        scrollName: 'scrollUp', // Element ID
	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
	        scrollFrom: 'top', // 'top' or 'bottom'
	        scrollSpeed: 300, // Speed back to top (ms)
	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
	        animation: 'fade', // Fade, slide, none
	        animationSpeed: 200, // Animation in speed (ms)
	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
					//scrollTarget: false, // Set a custom target element for scrolling to the top
	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
	        scrollTitle: false, // Set a custom <a> title if required.
	        scrollImg: false, // Set true to use image
	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	        zIndex: 2147483647 // Z-Index for the overlay
		});
	});
});



const religionDataBox = document.getElementById('religion-data-box')
const religionInput = document.getElementById('religion')


const casteDataBox = document.getElementById('caste-data-box')
const casteInput = document.getElementById('caste')

$.ajax({
    type: 'GET',
    url: '/religion-json/',
    success: function(response){
        console.log(response.data)
        const religionData = response.data
        religionData.map(item=>{     
            const option = document.createElement('option')
            option.textContent = item.name 
            option.setAttribute('class', 'item')
            option.setAttribute('data-value',item.name)
            religionDataBox.appendChild(option)

        })
    },
    error: function(error){
        console.log(error)
    }
})

religionInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedreligion = e.target.value

    casteDataBox.innerHTML = "" 
    const option = document.createElement('option')
    option.textContent = "select..."
    
    option.setAttribute('data-value',"choose caste")
    casteDataBox.appendChild(option)

    $.ajax({
        type:'GET',
        url:`/caste-json/${selectedreligion}/`,
        success: function(response){
            console.log(response.data)
            const casteData = response.data
            casteData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.name  
                option.setAttribute('class', 'item')
                option.setAttribute('data-value',item.value)
                casteDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }

    })

})