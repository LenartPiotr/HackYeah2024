import { useState } from "react";
import { typeMap } from "../../constans";
import { Languages } from "../../enums";
import { FaRegEdit } from "react-icons/fa";
import { IoSaveSharp } from "react-icons/io5";
import { useMutation } from "react-query";
import axios from "axios";

const SummaryValue = ({type, value, category, language}: SummaryTypeProps) => {
    const [isEditOpen, setIsEditOpen] = useState(false)
    const [inputValue, setInputValue] = useState(value);

    const postEditData = async (data: {type: string, value: string, category: string}) => {
        const response = await axios.post(`http://127.0.0.1:8000/edit`, data);
        return response.data;
    };

    const mutation = useMutation(postEditData);

    const handleEdit = () => setIsEditOpen((prev) => !prev);

    const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => setInputValue(e.target.value)

    const handleSave = () => {
        setIsEditOpen((prev) => !prev);

        mutation.mutate({ type: type, value: value, category: category });
    };

    return (
        <div className='category-response-wrapper'>
            <div className='category-response-block'>
                <div className='category-type'>{typeMap[type as keyof typeof typeMap][language]}</div>
                <div className='category-response'>
                    {
                        isEditOpen ? (
                            <input 
                                type="text"
                                value={inputValue}
                                onChange={(e) => handleOnChange(e)}
                            />
                        )
                        : (inputValue) 
                    }
                </div>
            </div>
            {
                isEditOpen ? (
                    <div 
                        onClick={() => handleSave()}
                        className='edit-response-button'>
                        <IoSaveSharp 
                            size="20px"
                        />
                        {messages['save'][language]}
                    </div>
                ) : (
                    <div 
                        onClick={() => handleEdit()}
                        className='edit-response-button'>
                        <FaRegEdit 
                            size="20px"
                        />
                        {messages['edit'][language]}
                    </div>
                )
            }
        </div>
    )
};

const messages = {
    'edit': {
        'polish': 'Edytuj',
        'english': 'Edit',
        'ukrainian': 'Редагувати',
    },
    'save': {
        'polish': 'Zapisz',
        'english': 'Save',
        'ukrainian': 'зберегти'
    }
};

type SummaryTypeProps = {
    type: string,
    value: string,
    category: string,
    language: Languages
}

export default SummaryValue;