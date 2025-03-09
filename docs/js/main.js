// AWS サービス情報を保持しておく変数。
let awsServices = null;

// AWS サービス情報の JSON ファイルのパス。
const awsServicesJsonPath = "data/services.json";

// AWS サービス情報を取得する関数。
// fetch を使って JSON ファイルを取得し、取得した JSON データを返す。
const getAwsServices = async () => {
    const response = await fetch(awsServicesJsonPath);
    return await response.json();
};

// スクリプトが読み込まれたら、AWS サービス情報を取得する。
document.addEventListener("DOMContentLoaded", async () => {
    awsServices = await getAwsServices();
    console.log(awsServices);
});
