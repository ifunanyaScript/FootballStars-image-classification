Dropzone.autoDiscover = false;

function init() {
    let dropz = new Dropzone("#dropz", {
        url: "/",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    });
    
    dropz.on("addedfile", function() {
        if (dropz.files[1]!=null) {
            dropz.removeFile(dz.files[0]);        
        }
    });

    dropz.on("complete", function (file) {
        let imageData = file.dataURL;
        
        var url = "/api/classify_image";

        $.post(url, {
            image_data: file.dataURL
        },function(data, status) {

            console.log(data);
            if (!data || data.length==0) {
                $("#resultDiv").hide();
                $("#probabilityTable").hide();                
                $("#error").show();
                return;
            }
            let footballers = ["cristiano_ronaldo", "karim_benzema", "lionel_messi", "mohammed_salah", "robert lewandoski", "zlatan_ibrahimovic"];
            
            let server_response = null;
            let bestScore = -1;
            for (let i=0;i<data.length;++i) {
                let maxScoreForThisLabel = Math.max(...data[i].label_probability);
                if(maxScoreForThisLabel>bestScore) {
                    server_response = data[i];
                    bestScore = maxScoreForThisLabel;
                }
            }
            if (server_response) {
                $("#error").hide();
                $("#resultDiv").show();
                $("#probabilityTable").show();
                $("#resultHolder").html($(`[data-player="${match.label}"`).html());
                let labelDict = server_response.label_dict;
                for(let footballer in labelDict) {
                    let item = labelDict[footballer];
                    let probabilityScore = server_response.label_probability[item];
                    let idName = "#probab_" + footballer;
                    $(idName).html(probabilityScore);
                }
            }
            // dropz.removeFile(file);            
        });
    });

    $("#submitButton").on('click', function (e) {
        dropz.processQueue();		
    });
}

$(document).ready(function() {
    console.log( "ready!" );
    $("#error").hide();
    $("#resultDiv").hide();
    $("#probabilityTable").hide();

    init();
})

/* ifunanyaScript */