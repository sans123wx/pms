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
        var item_id = button.data('id')
        $('.modal-title').text('修改记录')
        $('.modal-body').html('<p>请输入密匙</p><input type="password" name="key"><input hidden name="item_id" value="' + item_id + '">')
        $('form').attr('action' , '/edit_record')
        $('form').attr('method' , 'GET')
        }
    if(button.attr('name') == 'delete'){
        var item_id = button.data('id')
        $('.modal-title').text('删除记录')
        $('.modal-body').html('<p>请输入密匙</p><input type="password" name="key"><input hidden name="item_id" value="' + item_id + '">')
        $('form').attr('action' , '/delete_record')
        $('form').attr('method' , 'POST')
        
    }
})
