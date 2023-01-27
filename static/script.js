const input = document.querySelector('input');
const names = document.getElementsByTagName('li');
const name_list = document.getElementById('name_list');
const manage_button = document.getElementById('manage');
const popup = document.getElementsByClassName('pop_up')[0];
const prompt = document.getElementsByClassName('prompt')[0];
let manage = false;
let element = 'none';
function search(){
for (var i=0;i<names.length;++i){
 var name = names[i];
 if (name.innerText.toLowerCase().includes(input.value.toLowerCase())){
  name.style.display = 'flex';
 }
 else{
  name.style.display = 'none';
 };
};
};
function manage_function(){
if (manage){
    manage = false;
    name_list.classList.remove('display_list_manage');
    name_list.classList.add('display_list');
    manage_button.innerText = 'Manage';
}
else{
    manage = true;
    name_list.classList.remove('display_list');
    name_list.classList.add('display_list_manage');
    manage_button.innerText = 'Cancel';
};
};
function delete_prompt(id,name,elem){
    var func = 'element.remove();httpGet("/delete/" +' + id + ');popup.style.display="none";';
    element = elem;
    popup.style.display = 'flex';
    prompt.innerHTML = "<h2> Are you sure you want to delete " + name + "? </h2><div class='actions_prompt'><button onclick='" + func + "'> Yes </button><button onclick='popup.style.display=`none`;'> Cancel </button>";
};
function edit_prompt(id,name,elem){
   window.location.href = '/edit/' + id;
};

function httpGet(theUrl)
{
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", theUrl, false );
xmlHttp.send( null );
return xmlHttp.responseText;
}