$('.view_detail').click(function(){
    $('#myModal').modal('show')
    $('.modal-title').text('查看密码信息')
    $('.modal-body').html('<label>&nbsp;请输入密匙:&nbsp;&nbsp;&nbsp;</label><input type="password" name="key">')
    $('form').attr('action' , '/view_detail')
    $.ajax({
        url:'/account/ajax_post_captcha',
        type:'get',
        success:function(data){
            $('.modal-body').append(data)
        }
    })
})
$(document).on('click','.captcha',function(){
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
})