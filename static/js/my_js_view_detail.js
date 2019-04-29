// 表格初始值
$(function () {
    $('#table').DataTable({
      'paging'      : false,
      'lengthChange': false,
      'searching'   : true,
      'ordering'    : false,
      'info'        : false,
      'autoWidth'   : true,
    })
});
// 弹框内容设置

$('#myModal').on('show.bs.modal' , function(e){
    var button = $(e.relatedTarget)
    if(button.attr('name') == 'edit'){      
        $("button[name='submit']").attr('id' , 'edit')
        var item_id = button.data('id')
        $.ajax({
            url:'/upload/edit_sec',
            type: 'get',
            data: {'item_id':item_id,key:'key'},
            success: function(data){
                $('.modal-body').html(data)
                $('#id_title').val($(button).parent().prevAll().filter("[name='title']").text())
                $('#id_ip').val($(button).parent().prevAll().filter("[name='ip']").text())
                $('#id_sec').val($(button).parent().prevAll().filter("[name='sec']").text())
                $('#id_app_user_name').val($(button).parent().prevAll().filter("[name='app_user_name']").text())
                $('#id_app_sec').val($(button).parent().prevAll().filter("[name='app_sec']").text())
            }
        })
    }
    if(button.attr('name') == 'delete'){
        var item_id = button.data('id')
        $("button[name='submit']").attr('id' , 'delete')
        $("button[name='submit']").data('id' , item_id)
        $('.modal-title').text('删除记录')
        $('.modal-body').text('确定删除记录吗?')
        
    }
})