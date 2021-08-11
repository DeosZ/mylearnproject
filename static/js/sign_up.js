$(document).ready(function () {
    let correct1 = false;
    let correct2 = false;
    let correct3 = false;
    let correct4 = true;

    let regEx1 = /^[a-zA-Z][a-zA-Z0-9-\_\.]{5,19}$/;  // - регулярные выражения для проверки логина
    let regEx2 = /^[a-zA-Z0-9_]{8,}$/;  // - регулярные выражения для проверки пароля
    let regEx3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;  // - регулярные выражения для проверки емайла

    $('#login').blur(function () {
        login_x = $$('#login').val();
        if (regEx1.test(login_x)) {
            // - проверка занятости логина
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + login_x,
                success: function (result) {
                    if (result.message === 'занят') {
                        $('#login-mess').html('логин занят');
                        correct1 = false;
                    } else {
                        correct1 = true;
                        $('#login-mess').html('');
                    }
                }
            })
            correct1 = true;
            $('#login-mess').html('');
        } else {
            correct1 = false;
            $('#login-mess').html('Логин не соответствует шаблону валидации!');
        }
    });


    $('#pass1').blur(function () {
        pass1_x = $$('#pass1').val();
        if (regEx2.test(pass1_x)) {
            correct2 = true;
            $('#pass1-mess').html('');
            // - проверка занятости пароля
        } else {
            correct2 = false;
            $('#pass1-mess').html('Пароль не соответствует шаблону валидации!');
        }
    });


    $('#pass2').blur(function () {
        pass1_x = $$('#pass1').val();
        pass2_x = $$('#pass2').val();
        if (pass1_x === pass2_x) {
            correct3 = true;
            $('#pass2-mess').html('');
            // - проверка занятости пароля
        } else {
            correct3 = false;
            $('#pass2-mess').html('Пароли не совпадают');
        }
    });

    // проверка емайл дз за 10/08


    $('#submit').click(function () {
        if (correct1 === true && correct2 === true && correct3 === true && correct4 === true) {
            $('#form1').attr('onesubmit', 'return true');
        } else {
            $('#form1').attr('onesubmit', 'return false');
            alert('Форма содержит некоректные данные\n Отправка данных заблокирована.');
        }
    });

});