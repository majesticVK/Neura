$(document).ready(function () {
  // Initialize text animation for the main text
  $(".text").textillate({
      loop: true,
      sync: true,
      in: {
          effect: "bounceIn", // Animation effect for text entry
      },
      out: {
          effect: "bounceOut", // Animation effect for text exit
      },
  });

  // Initialize SiriWave animation
  var siriWave = new SiriWave({
      container: document.getElementById("Siri-Container"),
      width: 800,
      height: 200,
      style: "ios9",
      amplitude: "1",
      speed: "0.30",
      autostart: true,
  });

  // Button click event for microphone button
  $("#MicBtn").click(async function () {
      $("#Oval").attr("hidden", true); // Hide the oval
      $("#SiriWave").attr("hidden", false); // Show the wave animation
      console.log("Before taking command");
      const query = await eel.take_command()();  // Wait for the command
      console.log("After taking command:", query);
      if (query) {
          const response = await eel.allCommands(query)();  // Send the recognized query and get response
          if (response) {
              // Animate and display the response in your chat UI
              $("#chatbox").val(response);  // Assuming chatbox is where you want to show the response
              // Animate the response
              $(".response").text(response).textillate({
                  in: {
                      effect: 'fadeInUp', // Animate on response entry
                  },
                  out: {
                      effect: 'fadeOutDown', // Animate on response exit
                  },
              });
          }
      }
  });

  // Function to handle keyup event for text input
  function doc_keyUp(e) {
      if (e.key === 'j' && e.metaKey) {
          eel.playAssistantSound(); // Play assistant sound
          $("#Oval").attr("hidden", true);
          $("#SiriWave").attr("hidden", false);
          eel.allCommands()();  // Call allCommands function
      }
  }
  document.addEventListener('keyup', doc_keyUp, false);

  function ShowHideButton(message) {
    if (message.length == 0) {
        $("#MicBtn").attr('hidden', false);  // Show microphone button
        $("#SendBtn").attr('hidden', true);  // Hide send button
    } else {
        $("#MicBtn").attr('hidden', true);   // Hide microphone button
        $("#SendBtn").attr('hidden', false);  // Show send button
    }
}

// Key up event handler on the text box
$("#chatbox").keyup(function () {
    let message = $("#chatbox").val();  // Get the current message in the chatbox
    ShowHideButton(message);  // Call function to show/hide buttons
});

// Send button event handler
$("#SendBtn").click(function () {
    let message = $("#chatbox").val();  // Get the message from the chatbox
    if (message) {  // Only proceed if there is a message
        PlayAssistant(message);  // Function to process the message
        $("#chatbox").val('');  // Clear the chatbox after sending the message
        ShowHideButton('');  // Update button visibility
    }
});

// Enter key event to send message
$("#chatbox").keypress(function (e) {
    if (e.which == 13) {  // If the Enter key is pressed
        e.preventDefault();  // Prevent default form submission
        let message = $("#chatbox").val();  // Get the message
        if (message) {  // Only proceed if there is a message
            PlayAssistant(message);  // Function to process the message
            $("#chatbox").val('');  // Clear the chatbox after sending
            ShowHideButton('');  // Update button visibility
        }
    }
});
});
