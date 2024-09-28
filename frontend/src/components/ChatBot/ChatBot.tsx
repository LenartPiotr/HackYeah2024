import "./ChatBox.scss";

const messages = [
  {text: "Witaj", fromUser: true},
  {text: "Co tam", fromUser: false},
  {text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. At recusandae minus id nisi reprehenderit tenetur sit enim quasi similique ab non, tempore, debitis commodi in quas ipsum eaque architecto! Nemo.", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
  {text: "Co tam", fromUser: false},
];

const ChatBot = () => {
  return (
    <div className="chat-box">
      <div className="messages">
        {messages.map(message => <>
          <div className={`message-wrapper ${message.fromUser ? "from-user" : ""}`}>
            {!message.fromUser && <div className="avatar"></div>}
            <span className="message">
              {message.text}
            </span>
          </div>
        </>)}
      </div>
      <div className="input-row">
        <div className="input-wrapper">
          <input />
          <button className="send">-&gt;</button>
        </div>
        <button className="mic">X</button>
      </div>
    </div>
  )
};

export default ChatBot;