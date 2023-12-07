import PressMe from './press-me'

function H1(props) {
	return (<h1>{props.text}</h1>);
}

export default function HomePage() {
	const classes = ['J3', 'S1', 'S2'];
	function doClick() {
	setN(n + 1)
	console.log(`Yoo!, I was Clicked ${n}`);}
	return (<div>
		<H1 text="something..."/>
		<ul>{classes.map((i) => (<li key={i}>{i}</li>))}</ul>
		<PressMe />
		</div>);
}
