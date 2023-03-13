function submit() {
  let m1 = document.getElementById("mark1").value;
  let m2 = document.getElementById("mark2").value;
  let m3 = document.getElementById("mark3").value;
  let m4 = document.getElementById("mark4").value;
  let m5 = document.getElementById("mark5").value;
  let m6 = document.getElementById("mark6").value;
  let m7 = document.getElementById("mark7").value;
  let m8 = document.getElementById("mark8").value;

  const grade_pt = [
    Math.ceil(m1 / 10) * 3,
    Math.ceil(m2 / 10) * 3,
    Math.ceil(m3 / 10) * 3,
    Math.ceil(m4 / 10) * 3,
    Math.ceil(m5 / 10) * 3,
    Math.ceil(m6 / 10) * 2,
    Math.ceil(m7 / 10) * 2,
    Math.ceil(m8 / 10) * 1,
  ];

  let sum = 0;
  grade_pt.forEach((ele) => {
    sum += ele;
  });
  let sgpa = sum / 20;
  sgpa =  sgpa.toFixed(2);

  document.getElementById("result").innerHTML = sgpa;
  //res.classList.toggle('hidden');
  // alert("haha");
}
