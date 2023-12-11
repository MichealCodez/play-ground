import { useState } from "react";

function Square({ player, click }) {
  return (
    <button className="square" onClick={click}>
      {player}
    </button>
  );
}

export default function Board() {
  const [next, setNext] = useState(true);
  const [players, setPlayers] = useState(Array(9).fill(null));
  const notNull = (value) => value != null;
  let notNullArr = players.filter(notNull);
  function handleClick(i) {
    if (players[i] || calculateWinner(players) || notNullArr.length > 8) {
      return;
    }
    const nextPlayers = players.slice();
    next ? (nextPlayers[i] = "X") : (nextPlayers[i] = "O");
    setNext(!next);
    setPlayers(nextPlayers);
  }

  const winner = calculateWinner(players);
  let status;

  if (winner) {
    status = winner + " Wins!";
  } else if (notNullArr.length > 8) {
    status = "Draw!";
  } else {
    status = (next ? "X" : "O") + "'s Turn";
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square player={players[0]} click={() => handleClick(0)} />
        <Square player={players[1]} click={() => handleClick(1)} />
        <Square player={players[2]} click={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square player={players[3]} click={() => handleClick(3)} />
        <Square player={players[4]} click={() => handleClick(4)} />
        <Square player={players[5]} click={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square player={players[6]} click={() => handleClick(6)} />
        <Square player={players[7]} click={() => handleClick(7)} />
        <Square player={players[8]} click={() => handleClick(8)} />
      </div>
    </>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
