// 表格初始值
$(function () {
    $('#table').DataTable({
        language: {
            search: "搜索:",
            "oPaginate": {
                "sPrevious": "上一页",
                "sNext": "下一页",
            },
        },
      'paging'      : true,
      'lengthChange': false,
      'searching'   : true,
      'ordering'    : false,
      'info'        : false,
      'iDisplayLength': 5,
    })
});
// 弹框内容设置

$('#myModal').on('show.bs.modal' , function(e){
    var button = $(e.relatedTarget)
    if(button.attr('name') == 'edit'){      
        var item_id = button.data('id')
        $('.modal-title').text('修改记录')
        $('.modal-body').html(' \
        <input hidden name="item_id" value="' + item_id +'">\
        <div class="form-group">\
            <label for="id_key" class="col-sm-2 control-label">密匙</label>\
            <div class="col-sm-7">\
                <input type="password" name="key" class="form-control" required id="id_key">\
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_title" class="col-sm-2 control-label">名称</label>\
            <div class="col-sm-7">\
                <input type="text" name="title" class="form-control" required id="id_title" value="' + $('#' + item_id).find('.title').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_ip" class="col-sm-2 control-label">ip</label>\
            <div class="col-sm-7">\
                <input type="text" name="ip" class="form-control" required id="id_ip" value="' + $('#' + item_id).find('.ip').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_username" class="col-sm-2 control-label">用户名</label>\
            <div class="col-sm-7">\
                <input type="text" name="username" class="form-control" required id="id_username" value="' + $('#' + item_id).find('.username').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_pw" class="col-sm-2 control-label">密码</label>\
            <div class="col-sm-7">\
                <input type="text" name="pw" class="form-control" required id="id_pw" value="' + $('#' + item_id).find('.pw').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_app_username" class="col-sm-2 control-label">应用登录名</label>\
            <div class="col-sm-7">\
                <input type="text" name="app_username" class="form-control" required id="id_app_username" value="' + $('#' + item_id).find('.app_username').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_app_pw" class="col-sm-2 control-label">应用登录密码</label>\
            <div class="col-sm-7">\
                <input type="text" name="app_pw" class="form-control" required id="id_app_pw" value="' + $('#' + item_id).find('.app_pw').text() + '"> \
            </div>\
        </div>\
        <div class="form-group">\
            <label for="id_note" class="col-sm-2 control-label">备注</label>\
            <div class="col-sm-7">\
                <input type="text" name="note" class="form-control" required id="id_note" value="' + $('#' + item_id).find('.note').text() + '"> \
            </div>\
        </div>\
        ')
        $('form').attr('action' , '/edit_record')
        }
    if(button.attr('name') == 'delete'){
        var item_id = button.data('id')
        $('.modal-title').text('删除记录')
        $('.modal-body').html('<p>请输入密匙</p><input type="password" name="key"><input hidden name="item_id" value="' + item_id + '">')
        $('form').attr('action' , '/delete_record')
    }
})
