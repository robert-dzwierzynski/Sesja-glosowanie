function genPDF(id){
        html2canvas (document.getElementById("pdf")) .then (function (canvas) {

          var imgData = canvas.toDataURL('image/png');

          var imgWidth = 190; //210
          var pageHeight = 295;
          var imgHeight = canvas.height * imgWidth / canvas.width;
          var heightLeft = imgHeight;

          var doc = new jsPDF('p', 'mm');
          var position = 10;

          doc.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
          heightLeft -= pageHeight;

          while (heightLeft >= 0) {
            position = heightLeft - imgHeight;
            doc.addPage();
            doc.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
            heightLeft -= pageHeight;
          }
          doc.save('glosowanie-uchwala-'+id+'.pdf');

            });﻿
    }