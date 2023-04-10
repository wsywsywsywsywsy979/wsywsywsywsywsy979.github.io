$('document').ready(function(){
    let arr = Array.from({length : 10}, (_, v) => v + 1)
    let arr2 = Array.from({length : 5}, (_, v) => v + 1)
    console.log(arr);
    const shuffleArray = arr => {
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
        }
    }
    const shuffleArray2 = arr2 => {
        for (let i = arr2.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = arr2[i];
          arr2[i] = arr2[j];
          arr2[j] = temp;
        }
    }
    shuffleArray(arr);
    shuffleArray2(arr2);

    console.log(arr);
    arr.slice(0,9).forEach(function(val,idx){
        var id = "#q" + val.toString();
        // var id = "#q1"
        $(id).remove();
    });
    arr2.slice(0,4).forEach(function(val,idx){
        var id = "#s" + val.toString();
        // var id = "#q1"
        $(id).remove();
    });
    console.log(arr);
})
