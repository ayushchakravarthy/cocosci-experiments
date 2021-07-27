var my_node_id;

// Consent to the experiment.
$(document).ready(function() {

  // do not allow user to close or reload
  dallinger.preventExit = true;

  var slider = document.getElementById("contrib")
  var output = document.getElementById("slider_label")
  output.innerHTML = slider.value

  slider.oninput = function() {
    output.innerHTML = this.value;
  }

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

  $("#submit-response").click(function() {

    var contrib = $("#contrib").val()

    $("#submit-response").addClass('disabled');
    $("#submit-response").html('Sending...');

    dallinger.createInfo(my_node_id, {contents: contrib, info_type: "Info"})
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
