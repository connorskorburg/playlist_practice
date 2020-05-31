// async function getData(){
//     const response = await fetch(`https://api.spotify.com/v1/users/connorskorburg`, {
//         "method": "GET",
//         "headers": {
//             "Authorization": "Bearer AQAxknfYooYyHPqaEwyH6j_f1fZIDuH8l855XxSEIVa_K_YY3BlsdtvP2jZwKEArrmCjYCS18mC8TmiRt9593a_evNP45Ym2NYk5HzaQP8B_ZFKZwmZn4zBYhqQIf85bOH5Cw8UuhLw5EqQe9MLpvNGA9Da6OI_IgfuRp_rLYO_wLob0M2MERCNaiQiyi4CPRQ",
//         }
//     });
//     const data = await response.json();
//     console.log(data);
// }
// // getData()
// function redirect(){
//     const cid = '93d03c51a99146ed992ca0175f68674b'
//     const secret = '92a2119255fb489bbfe6e2a054f8c4b5'
//     window.location = `https://accounts.spotify.com/authorize?response_type=code&client_id=${cid}&scope=playlist-modify-public&redirect_uri=http://localhost:8000`
// }
// function getToken(){
//     const cid = '93d03c51a99146ed992ca0175f68674b'
//     const secret = '92a2119255fb489bbfe6e2a054f8c4b5'
//     window.location = `https://accounts.spotify.com/api/token`
// }



// curl -H "Authorization: Basic OTNkMDNjNTFhOTkxNDZlZDk5MmNhMDE3NWY2ODY3NGI6OTJhMjExOTI1NWZiNDg5YmJmZTZlMmEwNTRmOGM0YjU=" -d grant_type=authorization_code -d code=AQDqrvS8tWW-YW4ZOPz1VAdNTcTpOTXE6SUlCrMVD6MXYkx6s6fTLvW95V4IcPrgBzKRLuXG6L1mYI_wn2tcPvQW_fK5bpGS64JhFO7c_hOc3s7QVtvg3loldNmGb8_1CXM8GYg3lAnsrUdQt0wXb4Wq3964safYpjcYJUYW0LX59VJJ3_zBj7rAHKpp0BMhqw -d redirect_uri=http://localhost:8000 https://accounts.spotify.com/api/token

// {"access_token":"BQADDQbiwBx4vW0GG0fOa-vGMyhamsjyp0vuSLXI-kMGYu_ircpGT8b_CLBWdDco94CCYx10wqFUdN2oOO3JXHMpmVCQnKYXEfXrl6HA2QXi-wrA4dx1k0fxIYHVE1kwUuxRBSCOjBCdnFRiJeS-mZxdkqRuXyixnX7bNwUWx8r-qOVw-eCdLPuk4Ho","token_type":"Bearer","expires_in":3600,"refresh_token":"AQDHIcuOVWqm6_JcDPAgMatsWw5SCvyzYBvg5V2qktVTGrAO7JScXEZSYZO5RwSTnbLE5L16PPtwiLVv1k_gELnOP4Ig1fu4Yi_NDJyhbjOq_2O66ZIS9CFBRC3vM9w8uis","scope":"playlist-modify-public"}