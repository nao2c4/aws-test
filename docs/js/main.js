/**
 *
 * AWS サービス情報を管理するモジュール。
 * このモジュールは AWS サービスデータを JSON ファイルから取得し、
 * ランダムなサービス情報を提供する機能を実装しています。
 *
 * @module awsServiceModule
 * @author nao2c4
 * @version 1.0.0
 * @description AWS サービス情報の読み込みと操作を行うモジュール。
 */

/**
 * AWS サービス情報を保持しておく変数。
 * @type {Object|null}
 */
let awsServices = null;

/**
 * AWS サービス情報を含む JSON ファイルへのパス。
 * @type {string}
 * @constant
 */
const awsServicesJsonPath = "data/services.json";

/**
 * 現在の問題の正解となる AWS サービスの名前。
 * @type {Object|null}
 */
let correctService = null;

/**
 * AWS サービスのデータを JSON ファイルから取得。
 * @async
 * @function getAwsServices
 * @returns {Promise<Object>} AWS サービスデータオブジェクトを解決する Promise。
 * @throws {Error} フェッチ操作が失敗した場合、または JSON パースが失敗した場合にエラーをスローします。
 */
const getAwsServices = async () => {
    const response = await fetch(awsServicesJsonPath);
    return await response.json();
};


/**
 * 指定した数のランダムなAWSサービスを取得。
 * @param {number} num - 取得するAWSサービスの数。
 * @returns {Array} - ランダムに選択されたAWSサービスの配列。
 * @description awsServices配列からランダムな連続したサービスを指定数だけ取得します。
 */
const getRandomAwsServices = (num) => {
    const start = Math.floor(Math.random() * (awsServices.length - num + 1));
    return awsServices.slice(start, start + num);
};

/**
 * 配列をシャッフルする。
 * @params {Array} array - シャッフルする配列。
 * @returns {Array} - シャッフルされた配列。
 */
const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};

/**
 * サービスを 5 個選び、HTML に表示する。
 * @function showAwsServices
 * @description ランダムに選ばれた 5 つの AWS サービスを表示します。
 */
const showAwsServices = () => {
    const services = shuffleArray(getRandomAwsServices(5));
    correctService = services[Math.floor(Math.random() * 5)];
    // 概要を表示。
    document.getElementById("question").textContent = correctService.description;
    // 選択肢を表示。
    services.forEach((service, i) => {
        const ratio = document.getElementById(`choice${i + 1}`);
        ratio.textContent = service.service;
    });
    // 結果をリセット。
    document.getElementById("result").textContent = "";
    // 強調を解除。
    document.getElementById("result").classList.remove("correct", "incorrect");
}

/**
 * 回答をチェックする。
 * @function checkAnswer
 * @description 回答が正しいかどうかをチェックします。
 */
const checkAnswer = () => {
    // #choices-form 内の ratio 要素の中で、チェックが入っている要素を取得。
    const checked = document.querySelector("#choices-form input:checked");
    // チェックが入っている要素がない場合は、処理を中断。
    if (!checked) {
        return;
    }
    // チェックされた要素のラベルと、正解のサービス名が一致するかどうかをチェック。
    if (checked.labels[0].textContent === correctService.service) {
        document.getElementById("result").textContent = "正解！";
        // 特定のクラスを追加して、正解の文字を強調。
        document.getElementById("result").classList.add("correct");
    } else {
        document.getElementById("result").textContent = "不正解…";
        // 不正解の場合は、正解のサービスを #wrong-services に追加。
        const wrongService = document.getElementById("wrong-services");
        // wrongService に追加して改行する。
        wrongService.textContent += `${correctService.service}\n`;
        // 特定のクラスを追加して、不正解の文字を強調。
        document.getElementById("result").classList.add("incorrect");
    }
    // チェックを外す。
    checked.checked = false;
};

// スクリプトが読み込まれたら、AWS サービス情報を取得する。
document.addEventListener("DOMContentLoaded", async () => {
    awsServices = await getAwsServices();
    console.log(awsServices);
    showAwsServices();
    // ボタンのクリックイベントを登録。
    document.getElementById("generate-question").addEventListener("click", showAwsServices);
    document.getElementById("check-answer").addEventListener("click", checkAnswer);
});
