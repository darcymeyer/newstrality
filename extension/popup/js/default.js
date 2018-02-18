$.get("https://api.newstrality.com", {
  url: window.location.href,
  data: {
    url: window.location.href
  },
  timeout: 5000,
  dataType: "application/json",
}).done(function(data) {
  var article_data = data[0];
  var ideology = article_data["ideology"];
  var analysis = article_data["analysis"];
  var quantized_ideology = Math.round((ideology + 1) * 5) + 1;
  var color = "#00ff00";
  var html_content = "<strong>error...</strong><br><small>something weird happened</small>"
  switch (quantized_ideology) {
    case 1:
      color = "#0000FF";
      html_content = "<strong>extremely</strong><br><small>left-leaning</small>";
      break;
    case 2:
      color = "#1900E5";
      html_content = "<strong>strongly</strong><br><small>left-leaning</small>";
      break;
    case 3:
      color = "#3300CC";
      html_content = "<strong>considerably</strong><br><small>left-leaning</small>";
      break;
    case 4:
      color = "#4C00B2";
      html_content = "<strong>somewhat</strong><br><small>left-leaning</small>";
      break;
    case 5:
      color = "#660099";
      html_content = "<strong>neutral</strong><br><small>generally balanced</small>";
      break;
    case 6:
      color = "#7F007F";
      html_content = "<strong>neutral</strong><br><small>generally balanced</small>";
      break;
    case 7:
      color = "#990066";
      html_content = "<strong>somewhat</strong><br><small>right-leaning</small>";
      break;
    case 8:
      color = "#B2004C";
      html_content = "<strong>considerably</strong><br><small>right-leaning</small>";
      break;
    case 9:
      color = "#CC0033";
      html_content = "<strong>strongly</strong><br><small>right-leaning</small>";
      break;
    case 10:
      color = "#E50019";
      html_content = "<strong>extremely</strong><br><small>right-leaning</small>";
      break;
  }

  $("#top-bar .spectrum" + quantized_ideology).addClass("extended-bar-top");
  $("#leaning h4").html(html_content);
  $("#leaning h4").css({
    "color": color
  });

  var quantized_analysis = Math.round(analysis * 4);
  var analysis_html = "<small>degree of analysis</small><br><strong>unknown</strong>";
  switch (quantized_analysis) {
    case 0:
      analysis_html = "<small>contains</small><br><strong>little opinion</strong>";
      break;
    case 1:
      analysis_html = "<small>contains</small><br><strong>minor opinion</strong>";
      break;
    case 2:
      analysis_html = "<small>contains</small><br><strong>some opinion</strong>";
      break;
    case 3:
      analysis_html = "<small>contains</small><br><strong>considerable opinion</strong>";
      break;
    case 4:
      analysis_html = "<small>contains</small><br><strong>mostly opinion</strong>";
      break;
  }

  $("#analysis h5").html(analysis_html)

  var topics_html = "";

  for (topic in article_data["topics"]) {
    var name = article_data["topics"][topic];
    var sentiment = Math.random() * 2 - 1;
    if (sentiment < 0) {
      topics_html += "<h6 class=\"text-danger\">&#9660; " + name + "</h6>"
    } else {
      topics_html += "<h6 class=\"text-success\">&#9650; " + name + "</h6>"
    }
  }

  $("#entities").html(topics_html);

  $(".hidden-initially").css({
    "display": "inherit"
  });

  console.log(quantized_ideology);
  console.log(article_data);
}).fail(function(XMLHttpRequest, textStatus, errorThrown) {
  $("#leaning h4").html("<strong>error...</strong><br><small>please try again shortly</small>");
  $("#leaning h4").addClass("text-danger");
});
