$.get("https://api.newstrality.com", {
    url: window.location.href,
    data: {url: window.location.href},
    timeout: 5000,
    dataType: "application/json",
  }).done(function(data) {
    var article_data = data[0];
    console.log(article_data);
  }).fail(function(XMLHttpRequest, textStatus, errorThrown) {
      $("#leaning h4").html("<strong>error...</strong><br><small>please try again shortly</small>");
      $("#leaning h4").addClass("text-danger");
  });
