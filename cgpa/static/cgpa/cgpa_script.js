function submit() {
    let  m1 = document.getElementById('mark1').value;
    let  m2 = document.getElementById('mark2').value;
    let  m3 = document.getElementById('mark3').value;
    let  m4 = document.getElementById('mark4').value;
    let  m5 = document.getElementById('mark5').value;
    let  m6 = document.getElementById('mark6').value;
    let  m7 = document.getElementById('mark7').value;
    let  m8 = document.getElementById('mark8').value;
    
    let cgpa = ((m1*26)+(m2*25)+(m3*25)+(m4*26)+(m5*25)+(m6*26)+(m7*24)+(m8*23))/200;
    
    
      
      document.getElementById('result').innerHTML = cgpa;
    //res.classList.toggle('hidden');
    // alert('haha');
    }
    
    