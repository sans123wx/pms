$('.view_detail').click(function(){
    $('#myModal').modal('show')
    $('.modal-title').text('查看密码信息')
    $('.modal-body').html('<p>请输入密匙</p><input type="password" name="key">')
    $('form').attr('action' , '/view_detail')
})