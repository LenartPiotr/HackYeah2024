import "./ChatBox.scss";
import { useEffect, useRef, useState } from "react";
import { MessageType } from '../../types';
import data from '../../mocks/chatbot-api.json';
import loadingGif from "../../assets/loading.gif";

const ChatBot = () => {
  const [chatData, setChatData] = useState<MessageType[]>([]);
  const [message, setMessage] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const messageBox = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setChatData(data);
  }, [data]);

  useEffect(() => {
    if(messageBox.current) {
      messageBox.current.scrollTop = messageBox.current.scrollHeight;
    }
  }, [chatData])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if(!message) {
      return;
    }

    setChatData(chatData => [...chatData, {text: message, fromUser: true}]);
    setIsLoading(isLoading => true);
    new Promise((res) => setTimeout(res, 1000))
      .then(() => {
        setChatData(chatData => [...chatData, {text: "BOT odpowiada"}]);
        setIsLoading(isLoading => false);
      });
    
    setMessage("");
  }

  const handleButton = () => {
    input.current?.focus();
  }

  return (
    <form onSubmit={handleSubmit} className="chat-box">
      <div className="messages" ref={messageBox}>
        {chatData.map((message, index) => <>
          <div key={index} className={`message-wrapper ${message.fromUser ? "from-user" : ""}`}>
            {!message.fromUser && <div className="avatar"></div>}
            <span className="message">
              {message.text}
            </span>
          </div>
        </>)}
        {isLoading && <img width="32" height="32" src={loadingGif} />}
      </div>
      <div className="input-row">
        <div className="input-wrapper">
          <input name="message" ref={input} value={message} onChange={(e) => setMessage(e.target.value)} autoComplete="off"/>
          <button className="send" onClick={handleButton}>-&gt;</button>
        </div>
        <button type="button" className="mic">X</button>
      </div>
    </form>
  )
};

export default ChatBot;