/**
 *
 * AWS サービス情報を管理するモジュール。
 * このモジュールは AWS サービスデータを JSON ファイルから取得し、
 * ランダムなサービス情報を提供する機能を実装しています。
 *
 * @module awsServiceModule
 * @author nao2c4
 * @version 1.0.0
 * @description AWS サービス情報の読み込みと操作を行うモジュール
 */

// モジュールのコード...
// AWS サービス情報を保持しておく変数。
let awsServices = null;

// AWS サービス情報の JSON ファイルのパス。
const awsServicesJsonPath = "data/services.json";

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

// スクリプトが読み込まれたら、AWS サービス情報を取得する。
document.addEventListener("DOMContentLoaded", async () => {
    awsServices = await getAwsServices();
    console.log(awsServices);
});
