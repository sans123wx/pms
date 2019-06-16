$('#submit').click(function(){
    $.ajax({
        url:'xxx',
        type: 'post',
        data: $('form').serialize(),
        success: function(data){
            if(data == 'success'){
                alert('创建完成')
            }
        }
    })
})