var my_node_id;
// set default value to whatever needed
var stimulus = 0;

// Consent to the experiment.
$(document).ready(function() {

    // do not allow user to close or reload
    dallinger.preventExit = true;

    // Print the consent form.
    $("#print-consent").click(function() {
        window.print();
    });

    // Consent to the experiment.
    $("#consent").click(function() {
        dallinger.allowExit();
        dallinger.goToPage('instructions/instruct-ready');
    });

    // Consent to the experiment.
    $("#no-consent").click(function() {
        dallinger.allowExit();
        window.close();
    });

    
    $('#submit-response').click(function() {
        var response = $('#slider-response').valueAsNumber;

        stimulus = response;

        $('#submit-response').addClass('disabled')
        $('#submit-response').html('Sending...')

        dallinger.createInfo(my_node_id, {contents: response, info_type: "Info"})
        .done(function (resp) {
            dallinger.allowExit();
            dallinger.goToPage('questionnaire');
        })
        .fail(function (rejection) {
            dallinger.allowExit();
            dallinger.error(rejection);
        });
    });
});

// Create the agent.
var create_agent = function() {
  // Setup participant and get node id
    $("#submit-response").addClass('disabled');
    dallinger.createAgent()
    .done(function (resp) {
        my_node_id = resp.node.id;
        $("#submit-response").removeClass('disabled');
    })
    .fail(function (rejection) {
        dallinger.allowExit();
        dallinger.error(rejection);
    });
};

function loaded() {
    var half_thumb_width = 7.5;
    var labels = [0, 5, 10];
    var prompt = "Enter a Contribution using the slider (you must move the slider before submitting)";    
    var pre_stimulus = "The mean from the previous generation: "

    var html = '<div id="response-stimulus">' + pre_stimulus + stimulus + '</div>';
    html += '<div class="response-container" style="position:relative; margin: 0 auto 3em auto; ';
    html += 'width:auto;';
    html += '">';

    html += '<input type="range" class="slider" value="5" min="0" max="10" step="1" id="slider-response"></input>';

    html += '<div>';
    for(var j=0; j < labels.length; j++){
      var label_width_perc = 100/(labels.length-1);
      var percent_of_range = j * (100/(labels.length - 1));
      var percent_dist_from_center = ((percent_of_range-50)/50)*100;
      var offset = (percent_dist_from_center * half_thumb_width)/100;
      html += '<div style="border: 1px solid transparent; display: inline-block; position: absolute; '+
      'left:calc('+percent_of_range+'% - ('+label_width_perc+'% / 2) - '+offset+'px); text-align: center; width: '+label_width_perc+'%;">';  
      html += '<span style="text-align: center; font-size: 80%;">'+labels[j]+'</span>';
      html += '</div>'
    }
    html += '</div>';
    html += '</div>';

    html += prompt;
    console.log(html)

    // add submit button
    html += '<button id="submit-response" class="submn-btn">Submit</button>';

    document.getElementById("main").innerHTML = html;
}
