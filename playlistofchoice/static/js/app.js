async function getData(){
    const response = await fetch(`https://api.spotify.com/v1/users/connorskorburg`, {
        "method": "GET",
        "headers": {
            "Authorization": "Bearer AQAxknfYooYyHPqaEwyH6j_f1fZIDuH8l855XxSEIVa_K_YY3BlsdtvP2jZwKEArrmCjYCS18mC8TmiRt9593a_evNP45Ym2NYk5HzaQP8B_ZFKZwmZn4zBYhqQIf85bOH5Cw8UuhLw5EqQe9MLpvNGA9Da6OI_IgfuRp_rLYO_wLob0M2MERCNaiQiyi4CPRQ",
        }
    });
    const data = await response.json();
    console.log(data);
}
// getData()
function redirect(){
    const cid = '93d03c51a99146ed992ca0175f68674b'
    const secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    window.location = `https://accounts.spotify.com/authorize?response_type=code&client_id=${cid}&scope=playlist-modify-public&redirect_uri=http://localhost:8000`
}
function getToken(){
    const cid = '93d03c51a99146ed992ca0175f68674b'
    const secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    window.location = `https://accounts.spotify.com/api/token`
}