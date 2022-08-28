function refreshAfterPost(){
    setTimeout(function(){
        location.reload();
        return false;
    }, 1000);

}

function pushTags(list){
    var rules = "";

    var w1 = document.getElementById('inputw1').value;
    var w = w1
    var li = document.createElement("li");
    var rule = document.createTextNode(w);
    li.appendChild(rule);

    var removeBtn = document.createElement("input");
    removeBtn.type = "button";
    removeBtn.value = "Remove";
    removeBtn.onclick = remove;
    li.appendChild(removeBtn);
    document.getElementById("list").appendChild(li);
}

function remove(e) {
  var el = e.target;
  el.parentNode.remove();
}