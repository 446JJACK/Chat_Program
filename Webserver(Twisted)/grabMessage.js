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
       //Success
       success: function() {
         //alert('message was stored!');
       }//end success
      });
  });
});

