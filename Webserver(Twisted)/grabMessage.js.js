$(document).ready(function() {
  $('#contact').on('submit',function(e) {
     var $message = $("input#message").val();
     e.preventDefault();
     //POST request
     $.ajax({
       type: 'POST',
       url: 'http://student.cs.plattsburgh.edu:8081/grab',
       datatype: 'text',
       data: {'message': $message},
       //Success function
       success: function() {
         //alert('message was stored!');
       }//end success
     
     });//end ajax
  }); //end form ready
});//end doc function

