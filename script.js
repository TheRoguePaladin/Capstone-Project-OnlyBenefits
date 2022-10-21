var StudentObj = function(){
    var obj =  new Object();
    obj.Name="";
    obj.Surname="";
    obj.Password="";
};
var FillItem = function(){
    obj.Surname = document.getElementById("signSurname").value;
    obj.Name = document.getElementById("signName").value;
    obj.Password = document.getElementById("floatingPassword").value;
    return obj;
};

var Save = function(){
    var obj = new StudentObj();
    obj = FillItem(obj);
    $.ajax({
        type: "POST",
        async: false,
        url: document.location.pathname + "/StudentSave",
        data: "{'obj': "+ JSON.stringify(obj) +"}",dataType: "json",
        success: function (result) {
            document.getElementById('signName').value = '';
            document.getElementById('signSurname').value = '';
            document.getElementById('floatingPassword').value ='';
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log('XHR ERROR ' + xhr.status);
            console.log('Full ERROR ' + xhr.responseText);
            alert("Could not load page");
        }
    });
}