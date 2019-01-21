function onOrderFoodCreate(event) {
    event.preventDefault();

    $("#food_edit_modal .modal-title").text('Добавить блюдо');
    $("#food_submit").text('Добавить');

    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));

    $('#id_food').val('');
    $('#id_amount').val('');

    foodForm.off('submit');

    foodForm.on('submit', function (e) {

        e.preventDefault();

        orderFoodFormSubmit(onCreateSuccess);
    });

    $('#food_edit_modal').modal('show');
}


function onFormSubmitError(response, status) {
    // выводим содержимое ответа и статус в консоль.
    console.log(response);
    console.log(status);

    // если ответ содержит ключ errors,
    // выводим его содержимое в специальный div в модалке
    if (response.errors) {
        $('#food_form_errors').text(response.errors.toString());
    }
}


function orderFoodFormSubmit(success) {

    let url = $('#food_form').attr('action');

    let data = {
        food: $('#id_food').val(),
        amount: $('#id_amount').val(),
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
    };

    $.ajax({
        url: url,
        method: 'POST',
        data: data,
        success: success,
        error: onFormSubmitError
    });
}


function onCreateSuccess(response, status) {

    console.log(response);
    console.log(status);

    let newFoodTr = $('<tr></tr>');

    let foodNameTh = $('<th></th>')
        .attr('id', 'order_food_name_' + response.pk)
        .data('food_pk', response.food_pk)
        .text(response.food_name)
    let foodAmountTd = $('<td></td>')
        .attr('id', 'order_food_amount_' + response.pk)
        .text(response.amount + ' шт.');
    let editLink = $('<a></a>')
        .addClass('edit_link btn btn-primary float-right')
        .attr('href', response.edit_url)
        .data('pk', response.pk)
        .text('Изменить')
        .click(onOrderFoodUpdate);
    let editTd = $('<td></td>')
        .append(editLink)
    let deleteLink = $('<a></a>')
        .addClass('btn btn-primary float-right')
        .attr('href', '#')
        .text('Удалить');
    let deleteTd = $('<td></td>')
        .append(deleteLink)


    newFoodTr
        .attr('id', 'order_food_' + response.pk)
        .append(foodNameTh)
        .append(foodAmountTd)
        .append(editTd)
        .append(deleteTd)

    $('#order_food_list').append(newFoodTr);

    $('#food_edit_modal').modal('hide');
}


// функция, которая обрабатывает успешный AJAX-запрос на изменение блюда
function onUpdateSuccess(response, status) {
    // выводим содержимое ответа и статус в консоль.
    console.log(response);
    console.log(status);

    // находим нужное блюдо на странице и меняем его данные на новые, пришедшие в ответе
    let pk = response['pk'];
    let food_name_span = $('#order_food_name_' + pk);
    food_name_span.text(response.food_name);
    food_name_span.data('food_pk', response.food_pk);
    $('#order_food_amount_' + pk).text(response.amount);

    // прячем модалку
    $('#food_edit_modal').modal('hide');
}


function onOrderFoodUpdate(event) {
    // отменяем действие по умолчанию (переход по ссылке)
    event.preventDefault();

    // меняем заголовок и текст на кнопке "Добавить" в модалке
    $("#food_edit_modal .modal-title").text('Изменить блюдо');
    $("#food_submit").text('Изменить');

    // меняем action в форме в модалке на url,
    // указанный в href нажатой ссылки на редактирование.
    // this в обработчиках событий указывает на тот объект,
    // к которому привязано событие, в данном случае -
    // на ту ссылку, которая была нажата.
    let foodForm = $('#food_form');
    foodForm.attr('action', $(this).attr('href'));

    // находим элементы с именем блюда и количеством блюда на странице,
    // используя свойство data-pk нажатой ссылки.
    let foodPk = $(this).data('pk');
    let foodName = $('#order_food_name_' + foodPk);  // '#order_food_name_1'
    let foodAmount = $('#order_food_amount_' + foodPk);  // '#order_food_amount_1'

    // задаём в форме исходные значения для данного блюда в заказе.
    // т.к. на странице выводится название блюда, а нам нужен его pk,
    // pk сохраняем и получаем через data-атрибут food_pk.
    $('#id_food').val(foodName.data('food_pk'));
    $('#id_amount').val(foodAmount.text());

    // отключаем предыдущие обработчики события отправки формы
    foodForm.off('submit');

    // задаём обработчик события отправки формы
    foodForm.submit(function (event) {
        // отменяем действие по умолчанию (обычная отправка формы)
        event.preventDefault();

        // отправить форму с помощью функции orderFoodFormSubmit, которая использует AJAX-запрос.
        // в случае успеха вызвать функцию onUpdateSuccess
        orderFoodFormSubmit(onUpdateSuccess);
    });

    // показываем модалку на экране.
    $('#food_edit_modal').modal('show');
}


window.addEventListener('load', function () {
    $('#food_submit').on('click', function (e) {
        $('#food_form').submit();
    });
    $("#order_food_add_link").click(onOrderFoodCreate);
    $('#order_food_list .edit_link').click(onOrderFoodUpdate);
});