function AutoClickConnect(){
	try{

		colab_button = document.querySelector('colab-connect-button')

		if (colab_button.childNodes[1].childNodes[1].childNodes[6] !== undefined){
			var_Reconnect = colab_button.childNodes[1].childNodes[1].childNodes[6].textContent.toString().trim();
			var_rec = var_Reconnect.substring(0, 9);
			if(var_rec === 'Reconnect'){
				colab_button.childNodes[1].childNodes[1].childNodes[6].click();
			}
		}
		else{
			var_Connect = colab_button.childNodes[1].childNodes[1].childNodes[3].childNodes[0].textContent.trim();
			if (var_Connect == 'Connect') {
				colab_button.childNodes[1].childNodes[1].childNodes[3].click()
			}
		}
	}
	catch(ex){
		console.log("No DOM")
	}
}

setInterval(AutoClickConnect, 10000)