let filesList = []
let appURL = 'http://127.0.0.1:8000';
function filesSelected(){
    let files = document.getElementById('filesselect').files;
    if (files.length > 0){
        filesList = files;
        readytouploadFiles(files)
    }
}

function readytouploadFiles(files){
    document.getElementById('filesuploadbox').style.display = 'none';
    document.getElementById('fileprogressbox').style.display = 'block';
    document.getElementById('files-data').innerHTML = '';
    for (let i=0;i<files.length;i++){
        let fileName = files[i].name;
        let tr = document.createElement('tr');
        let tdFileName = document.createElement('td');
        tdFileName.innerText = fileName;
        //  let tdProgress = document.createElement('td');
        // tdProgress.innerText = 0;
        tr.appendChild(tdFileName)
        // tr.appendChild(tdProgress)
        document.getElementById('files-data').appendChild(tr);
    }
}

function startUploading(){
    let formData = new FormData();
    for (let i=0;i<filesList.length;i++){
        formData.append('filesList', filesList[i]);
    }
    document.getElementById('cancel-btn').setAttribute('disabled', true);
    document.getElementById('start-btn').setAttribute('disabled', true);
    $.ajax({
                url: appURL + `/upload-files`,
                type: 'POST',
                dataType: "JSON",
                data: formData,
                contentType: false,
                cache: false,
                processData: false,
                 headers: { "X-CSRFToken": getCookie('csrftoken') },
                success: function (result) {
                    if (result.status === 1){
                        swal("Success!", "Files Uploaded! You can view your files in My files tab", "success").then((value) => {
                                 window.location.reload()
                        });

                    }else{
                         swal("Error!", result.message, "error").then((value) => {
                                 window.location.reload()
                        });
                    }
                },
                error: function (data) {
                        swal("Error!", "Server Error, please try again later", "error").then((value) => {
                                 window.location.reload()
                        });
                }
            });

}

function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie !== '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) === (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
 }