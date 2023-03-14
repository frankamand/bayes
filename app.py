import streamlit as st
import streamlit.components.v1 as components


p_h = 0
p_e_h = 0
p_e_nh = 0 


with st.sidebar:
    p_h = st.slider('Prior P(H) in %', 0, 100, 50)
    p_e_h = st.slider(' P(E|H) in %', 0, 100, 50)
    p_e_nh = st.slider(' P(E|¬H) in %', 0, 100, 50)



st.write("P(H)=", p_h/100)
st.write("P(E|H)=", p_e_h/100)
st.write("P(E|¬H)=", p_e_nh/100)

html_temp = """
<!DOCTYPE html>
<html>
<head>
	<title>Canvas Rectangle Example</title>
	<style>
		canvas {{
			background-color:lightgrey;
		}}
	</style>
</head>
<body>
	<canvas id="myCanvas" width="400" height="400"></canvas>

	<script>
		// Get the canvas element and context
		var canvas = document.getElementById("myCanvas");
		var ctx = canvas.getContext("2d");

		// Set the fill color to red
		ctx.fillStyle = "#17497b";

		// Draw a rectangle on the canvas
		ctx.fillRect(00, 00, {0}, 400 );
        ctx.fillStyle = "lightblue";
        ctx.fillRect(00 + {0}, 00, 400 - {0}, 400 );
        ctx.globalAlpha = 0.3;
        ctx.fillStyle = "red";
        ctx.fillRect(00 + {0},400 - {1}, 400 -{0},{1})
        ctx.fillRect(00, 400 -{2}, {0}, {2})
	</script>
</body>
</html>
""".format(4*p_h,4*p_e_nh,4*p_e_h)

p_h_e = round(((p_e_h/100) * (p_h/100))/((p_e_h/100)*(p_h/100) + (p_e_nh/100)*(1-(p_h/100))),2)

st.write("P(H|E)=",p_h_e)

# bootstrap 4 collapse example
components.html(html_temp, height=600)
