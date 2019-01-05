//window.alert("HELLO");

/*VALIDATION FOR ADD USER FORM*/
$(document).ready(function() {              //id of the form
    $('#aadhaarForm').bootstrapValidator({              //options of validator
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',            //icons
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
       

        continueButton: {
            notEmpty: {
                message: 'The aadhar number is required and cannot be empty'
            },
            stringLength: {
                min: 12,
                message: 'The aadhar number  must have at least 12 digits'
            }
        }
          
        } 
    });
});
