
//** 全選択処理 */
function checkAll(){
    const headerCheck = document.getElementById('headCheck');
    const dataCheck = document.getElementsByName('selected_products');
    
    if (headerCheck.checked){
        for(i = 0; i < dataCheck.length; i++) {
            dataCheck[i].checked = true;
          }
    }else{
        for(i = 0; i < dataCheck.length; i++) {
            dataCheck[i].checked = false;
        }
    }
}


const mainForm = document.getElementById("mainForm"); // formの値
const actionTypeInput = document.getElementById("actionType"); // アクションの種別
const selectedProductsInput = document.getElementById("selectedProducts"); // 選択された商品

const updateButton = document.getElementById("updateButton"); // 更新ボタン
const deleteButton = document.getElementById("deleteButton"); // 削除ボタン


/** 
 * 更新ボタン押下時の処理 
 */
updateButton.addEventListener("click", function () {
    // アクションタイプを更新に設定
    actionTypeInput.value = "update"; 
    // formのactionを設定
    mainForm.action = updateButton.getAttribute("data-update-url");
    // formを送信
    mainForm.submit();
});

/** 
* 削除ボタン押下時の処理 
*/
deleteButton.addEventListener("click", function () {
    // アクションタイプを削除に設定
    actionTypeInput.value = "delete";
    // formのactionを設定
    mainForm.action = deleteButton.getAttribute("data-delete-url");
    // formを送信
    mainForm.submit();
});



// 以下2つの処理は必要ではなくなった。
// フォームの送信処理は、削除処理更新処理でそれぞれ持たせることにしたため。
// 選択商品のID取得処理を使用しなくとも、HTMLのinputチェックボックスで設定したところでvalueを取得してformで送信できたため。
/** 
 *  フォームの送信処理
 */
function submitForm() {
    // 選択商品のID取得処理を呼び出す。
    const selectedIds = getSelectedIds();
    // 選択商品の値を取得したIDに設定する。
    selectedProductsInput.value = selectedIds;
    mainForm.submit();
}

/** 
 * 選択商品のID取得処理
 */
function getSelectedIds() {
    // インプットでチェックされたデータを取得する。
    // querySelectorAllメソッドはCSSのセレクターと同じ書き方でHTML要素を取得する
    const selectedCheckboxes = document.querySelectorAll("input[type=checkbox]:checked");
    // 
    const selectedIds = Array.from(selectedCheckboxes).map(checkbox => checkbox.value);
    return selectedIds.join(",");
}

