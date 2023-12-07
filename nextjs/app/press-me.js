'use client';

import {useState} from 'react'

export default function PressMe() {
	const [n, setN] = useState(1)
	function doClick() {
        setN(n + 1)
        console.log(`Yoo!, I was Clicked ${n}`);}
	return (<button onClick={doClick}>Press Me!</button>);	
}
