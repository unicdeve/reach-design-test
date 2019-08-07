$(document).ready(function () {

  $('.budget').hide();
  formAction = $('.budget-form').attr('action');
  console.log(formAction);
  $(document).on('submit', '#form', function (e) {
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: formAction,
      data: $('#form').serialize(),
      success: function (data) {
        console.log(data)

        $('.budget').show();
        Object.keys(data).forEach(function (item) {
          if (item === "groceries") {
            $('.groc_perc').html(`${Math.round(data["income"]/data[item])}%`);
            $('.groc_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "saving") {
            $('.savings').html(`${Math.round(data["income"]/data[item])}%`);
            $('.savings_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "clothing") {
            $('.cloth').html(`${Math.round(data["income"]/data[item])}%`);
            $('.cloth_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "healthcare") {
            $('.healthcare').html(`${Math.round(data["income"]/data[item])}%`);
            $('.healthcare_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "household_repair") {
            $('.household').html(`${Math.round(data["income"]/data[item])}%`);
            $('.household_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "laundry") {
            $('.laundry').html(`${Math.round(data["income"]/data[item])}%`);
            $('.laundry_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "subscriptions") {
            $('.subs').html(`${Math.round(data["income"]/data[item])}%`);
            $('.sub_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "miscellaneous") {
            $('.misc').html(`${data["income"]/data[item]}%`);
            $('.misc_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "rent") {
            $('.rent').html(`${data["income"]/data[item]}%`);
            $('.rent_amt').html(`${Math.round(data[item])}`);
          }

          if (item === "transport") {
            $('.trans').html(`${Math.round(data["income"]/data[item])}%`);
            $('.trans_amt').html(`${Math.round(data[item])}`);
          }
        });

        income: $('.income').val('')
        y_distance: $('#y_distance').val('')
      },
      error: function (error) {
        console.log(error.responseJSON)
        var jsonData = error.responseJSON
        var msg = ""

        $.each(jsonData, function (key, value) {
          msg += key + ": " + value + "<br/>"
        })

        $.alert({
          title: "Oops!",
          content: msg,
          theme: "modern",
        })
      }
    })
  })
});