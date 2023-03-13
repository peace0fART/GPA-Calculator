function submit() {
  let m1 = document.getElementById("mark1").value;
  let m2 = document.getElementById("mark2").value;
  let m3 = document.getElementById("mark3").value;
  let m4 = document.getElementById("mark4").value;
  let m5 = document.getElementById("mark5").value;
  let m6 = document.getElementById("mark6").value;
  let m7 = document.getElementById("mark7").value;
  let m8 = document.getElementById("mark8").value;

  let dict = {};

  // add values to the dictionary
  dict[m1] = 20;
  dict[m2] = 20;
  dict[m3] = 24;
  dict[m4] = 24;
  dict[m5] = 25;
  dict[m6] = 24;
  dict[m7] = 20;
  dict[m8] = 18;

  for (const [key, value] of Object.entries(dict)) {
    if (key == "") {
      delete dict[key];
      console.log(dict);
    }
  }
  let sum = 0;
  let denom = 0;
  let cgpa = 0;

  for (const [key, value] of Object.entries(dict)) {
    sum += key * dict[key];
    denom += value;
    cgpa = sum / denom;
  }
  // let cgpa = ((m1*26)+(m2*25)+(m3*25)+(m4*26)+(m5*25)+(m6*26)+(m7*24)+(m8*23))/200;
  cgpa = cgpa.toFixed(2);
  document.getElementById("result").innerHTML = cgpa;
  //res.classList.toggle('hidden');
  // alert('haha');
}