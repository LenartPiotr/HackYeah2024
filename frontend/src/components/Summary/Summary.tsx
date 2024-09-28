import './summary.scss';
import data from '../../mocks/summary-api.json';
import { useEffect, useState } from 'react';
import { SummaryType } from '../../types';
import { categoryMap, typeMap } from '../../constans';
import { FaRegEdit } from "react-icons/fa";

const Summary = () => {
    const [summaryData, useSummaryData] = useState<SummaryType[]>([]);

    useEffect(() => {
        useSummaryData(data);
    }, [data]);

    const categories = new Set(summaryData.map((summary: SummaryType) => summary.category));

    const summaryElements = [...categories].map((category: string) => {
        
        const categoryData = summaryData
            .filter((summary: SummaryType) => summary.category === category)
            .map((summary: SummaryType) => (
                <div className='category-response-wrapper'>
                    <div className='category-response-block'>
                        <div className='category-type'>{typeMap[summary.type as keyof typeof typeMap]}</div>
                        <div className='category-response'>{summary.response}</div>
                    </div>
                    <div className='edit-response-button'>
                        <FaRegEdit 
                            size="20px"
                        />
                        Edytuj
                    </div>
                </div>
            ))

        return (
            <div className='summary-category'>
                <h3 className='category-header'>{categoryMap[category as keyof typeof categoryMap]}</h3>
                <div className='category-data'>
                    {...categoryData}
                </div>
            </div>
        )
    });

    return (
        <div className='main-summary'>
            <h2 className='summary-title'>Podsumowanie</h2>
            {...summaryElements}
            <button className='summary-accept'>Akceptuj i zapisz</button>
        </div>
    )
};

export default Summary;